# conding:utf8
import configparser

__author__ = u'奶茶哥'

if __name__ == '__main__':

    # ini文件读写
    
    # 先构建一个对象
    config = configparser.ConfigParser()

    # 写入几组数据
    # 先创建一个section
    config.add_section('软件测试')

    # 在新建的section下加key-value键值对
    config.set('软件测试','自动化','selenium')
    config.set('软件测试','性能','jmeter')
    config.set('软件测试','接口','soapui')

    # 再新增一个section，但不加key-value值
    config.add_section('没有测试技术')

    # 写入文件
    with open('iniConfig.ini','w') as configfile:
        config.write(configfile)

    ##########################################
    # 把ini文件内容读取出来
    config.read('iniConfig.ini')
    # 获取所有的sections
    sections = config.sections()
    print(sections)

    # 获取section下所有的options
    for sec in sections:
        options = config.options(sec)
        print(options)

    # 根据sections和options获取对应的value值
    for sec in sections:
        for option in config.options(sec):
            print('[%s] %s=%s ' % (sec,sections,
                                   config.get(sec,option)))


















