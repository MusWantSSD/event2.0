## 使用说明
1. 安装依赖requirements中所需包
2. 将 utils/get_cookie.py 中，data里的 username 及 password 修改为自己的值
3. 先运行一次 utils/get_cookie.py ，失败则多试几次，若cookie过期后再次运行即可
4. 运行 main.py 可以自动报名一切可以报名的活动
5. 完成报名后会获得已报名活动的 hdid 及 id 列表
6. 将**id**列表中，希望保留的活动id值删除，剩下的列表作为 event_cancel 的输入，完成其余报名活动的取消
