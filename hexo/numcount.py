from functools import reduce

import gitlab

url = '124.127.40.85:9000'
private_token = 'x_gc9X7A1qzAN_3xV41A'

# 登录 获取gitlab操作对象gl
gl = gitlab.Gitlab(url, private_token)
# 获取所有的用户列表
# users = gl.users.list()
# for user in users:
#     print('所有用户：',user.name)
# users = gl.users.list(all=True)

# list all the projects
start_time = '2020-09-02T00:00:00Z'
end_time = '2020-09-03T00:00:00Z'


def getAllWorkLine():
    '''获取所有人的工作量'''
    projects = gl.projects.list(all=True)
    short_id_list = []
    name_list = []
    for project in projects:
        # print('项目名：', project.name)
        branches = project.branches.list()
        for branch in branches:
            # print('分支名：', branch.name)
            commits = project.commits.list(all=True, query_parameters={'since': start_time, 'until': end_time,
                                                                       'ref_name': branch.name})
            for commit in commits:
                com = project.commits.get(commit.id)
                # com = commit
                # print('-----------------start-------------')
                # print('备注：',com)
                # print('备注：',com.message)
                if (com.short_id in short_id_list):
                    # print('跳过merge产生的commit')
                    break
                # print('项目名：', project.name)
                # print('分支名：', branch.name)
                # {'additions': 129, 'deletions': 22, 'total': 151}
                # print('提交信息:',com.author_name,com.stats)
                name = com.author_name
                total = com.stats['additions']
                r = {
                    'name': name,
                    'total': total,
                }
                if len(name_list) > 0:
                    for n in name_list:
                        # print(n['name'],name)
                        ishave = False
                        if n['name'] == name:
                            n['total'] = n['total'] + total
                            ishave = True
                            break
                    # print(ishave)
                    if not ishave:
                        name_list.append(r)
                else:
                    name_list.append(r)
                short_id_list.append(com.short_id)

    print('name', name_list)
    # print('-----------------end-------------')


def getAllIssues():
    projects = gl.projects.list(all=True)
    for project in projects:
        print('项目名：', project.name)
        # branches = project.branches.list()
        issues = project.issues.list(all=True, query_parameters={'since': '2020-05-20T00:00:00Z',
                                                                 'until': '2020-05-21T00:00:00Z'})
        for issue in issues:
            print(issue)
        break


getAllWorkLine()
