# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import time
from multiprocessing import Queue
from server.URLManager import URLManager
from server.DataOutput import DataOutput
from multiprocessing.managers import BaseManager
from multiprocessing import Process


class ControlManager(object):

    def start_manager(self, url_q, result_q):
        BaseManager.register('get_task_queue', callable=lambda: url_q)
        BaseManager.register('get_result_queue', callable=lambda: result_q)
        manager = BaseManager(address=('', 8001), authkey='baike')
        return manager


    def url_manager_proc(self, url_q, conn_q, root_url):
        url_manager = URLManager()
        url_manager.add_new_url(root_url)
        while True:
            while(url_manager.has_new_url()):
                new_url = url_manager.get_new_url()
                url_q.put(new_url)
                print "old_url=", url_manager.old_url_size()
                if(url_manager.old_url_size() > 200):
                    url_q.put('end')
                    print "控制节点发起结束通知"
                    url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt', url_manager.old_urls)
                    return
            try:
                if not conn_q.empty():
                    urls = conn_q.get()
                    url_manager.add_new_urls(urls)
            except Exception as e:
                time.sleep(0.1)

    def result_solve_proc(self, result_q, conn_q, store_q):
        while(True):
            try:
                if not result_q.empty():
                    print "get result of q"
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        print "结果分析进程接收通知后结束"
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])
                    store_q.put(content['data'])
                else:
                    time.sleep(0.1)
            except BaseException as e:
                time.sleep(0.1)

    def store_proc(self, store_q):
        output = DataOutput()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == "end":
                    print "存储进程接收通知然后结束"
                    output.output_end(output.filepath)
                    return
                output.store_data(data)
            else:
                time.sleep(0.1)


if __name__ == "__main__":
    url_q = Queue()
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()
    node = ControlManager()
    manager = node.start_manager(url_q, result_q)
    url_manager_proc = Process(target=node.url_manager_proc, args=(url_q, conn_q, 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB',))
    result_solve_proc = Process(target=node.result_solve_proc, args=(result_q, conn_q, store_q, ))
    store_proc = Process(target=node.store_proc, args=(store_q,))
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    manager.get_server().serve_forever()