import jenkins

server = jenkins.Jenkins('http://localhost:8080', 
                         username='adam', 
                         password='1184577b709915135451ec5a6797470ba6')

user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version)) 

# CREATE JOB
# server.create_job("JOB1",jenkins.EMPTY_CONFIG_XML)

# CREATR PRE CONFIGURED JOB
# job2_xml = open("job2.xml", mode='r', encoding='utf-8').read()
# server.create_job("JOB2",job2_xml)

# COPY JOB
# server.copy_job('JOB2','JOB3')

# # DISABLE JOB
# server.disable_job('JOB3')

# RUN AND BUILD
# server.build_job('JOB2')
# last_build = server.get_job_info('JOB2')['lastCompletedBuild']['number']
# build_info = server.get_build_info('JOB2',last_build)
# print("BUiLD NUMBER ",last_build)
# print("BUiLD INFO ",build_info)

# DELETE JOB
server.delete_job('JOB3')