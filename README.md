# XMind2Xls

> **XMind2Xls** 工具，提供了从思维导图格式转换成Excel格式的解决方案


### 一、背景

软件测试过程中，最重要、最核心就是测试用例的设计。
而实施情况并非如此，实际上在测试活动过程中书写测试用例占用了大量的重复性劳动时间。特别是在敏捷开发模式下，以下的痛点暴露的尤为明显。

- 1、将大量的测试用例组织到Excel内进行案例评审，会带来内容冗余，组织层级不立体，过程繁琐，更新效率低，对参加评审的与会人员造成视觉疲劳...
- 2、快速迭代周期内，书写测试用例时间严重挤占了案例设计的时间。造成案例覆盖率不足，遗漏；
- 3、需求变更后，excel内的案例更新不完整，不利于集成测试的开展；
- 4、...

基于这些情况，现在越来越多公司选择使用**思维导图**这种高效的生产力工具进行用例设计，特别是敏捷开发团队。

但是与此同时，使用思维导图进行测试用例设计的过程中也带来不少问题：
- 1、测试用例难以量化管理、执行情况难以统计；
- 2、测试用例执行结果与BUG管理系统难以打通；
- 3、团队成员用思维导图设计用例的风格各异，沟通成本巨大；
- 4、...

### 二、设计思路
综合以上的优劣情况，我们能不能将xmind 和 excel 结合起来。在提升效率的同时，兼顾到实用的效果

## 我的设计思路是这样的：
![flowchart](https://github.com/taoyu0429/xmid2excel/blob/master/flowchart.png?raw=true)




### 三、环境搭建

#### 1、安装python
https://jingyan.baidu.com/article/25648fc19f61829191fd00d4.html

#### 2、运行命令行安装xmind2xls
```
pip3 install xmind2xls
```

### 四、使用方式

#### 1、新建模版
![xmind-demo](https://github.com/taoyu0429/xmid2excel/blob/master/xmind-demo.png?raw=true)

#### 2、编辑模版

#### 3、运行命令行
```
 xmind2xls [path_to_xmind_file] [-xlsx]
```
#### 4、在模版同目录下查看excel结果
![xmind-demo](https://github.com/taoyu0429/xmid2excel/blob/master/result-demo.png?raw=true)


### 五、版本升级
```
pip3 install -U xmind2xls

```
### 六、致谢
**XMind2Xls** 工具的产生，受益于以下两个开源项目，并在此基础上扩展、优化。

- 1、**[XMind](https://github.com/zhuifengshen/xmind)**：XMind思维导图创建、解析、更新的一站式解决方案(Python实现)！  
- 2、**[xmind2testcase](https://github.com/zhuifengshen/xmind2testcase)**：践行了XMind通用测试用例模板设计思路，同时提供了Web转换工具！

### 七、持续集成部署
```
为了应对后期项目的维护和持续优化，本项目引入了travis+github的持续集成部署模式
每次本地代码打上tag推送到github仓库后，travis会自动触发构建、测试、部署到pypi等操作
欢迎有志于持续改进测试流程和提高效率的小伙伴为本项目添砖加瓦
```
### LICENSE
```
MIT License
Copyright (c) 2019 taoyu
Copyright (c) 2019 Devin https://zhangchuzhao.site
Copyright (c) 2017 Toby Qin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


