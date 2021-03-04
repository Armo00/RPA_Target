<template>
    <el-container class="home-container">
        <!-- 头部区域 -->
        <el-header>
            <div>
                <img src="../assets/shu.jpg" alt="" height="60px">
                <span>运单填报管理系统</span>
            </div>
            <div class="welcomeBox">
                欢迎！{{UserNameX}}
                <el-button type="info" @click="logout">退出</el-button>
            </div>
            
        </el-header>
        <!-- 页面主体区 -->
        <el-container>
            <!-- 侧边栏 -->
            <el-aside :width="isCollapse ? '64px' : '200px'">
                <div class="toggle-button" @click="toggleCollapse">|||</div>
                <!-- 侧边栏菜单区域 -->
                <el-menu background-color="#333744"
                         text-color="#fff"
                         active-text-color="#409EFF"
                         :collapse="isCollapse"
                         :collapse-transition="false"
                         router
                         :default-active="$route.path">

                    <el-submenu index="1" >
                        <template slot="title">
                            <i class="el-icon-document"></i>
                            <span>填报</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="/filling">
                                <template slot="title">
                                    <i class="el-icon-rank"></i>
                                    <span>发票</span>
                                </template>
                            </el-menu-item>
                        </el-menu-item-group>

                    </el-submenu>

                    <el-submenu index="2">
                        <template slot="title">
                            <i class="el-icon-menu"></i>
                            <span>修改飞机</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="/modifyHub">
                                <template slot="title">
                                    <i class="el-icon-rank"></i>
                                    <span>更改hub</span>
                                </template>
                            </el-menu-item>
                            <el-menu-item index="/modifyModel">
                                <template slot="title">
                                    <i class="el-icon-share"></i>
                                    <span>更改构型</span>
                                </template>
                            </el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>

                    <el-submenu index="4">
                        <template slot="title">
                            <i class="el-icon-document"></i>
                            <span>自动化助手</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="/autoPurchase">
                                <template slot="title">
                                    <i class="el-icon-s-tools"></i>
                                    <span>全自动购买(测试)</span>
                                </template>
                            </el-menu-item>
                            <el-menu-item index="/autoPlanning">
                                <template slot="title">
                                    <i class="el-icon-date"></i>
                                    <span>自动排班</span>
                                </template>
                            </el-menu-item>

                            <el-menu-item index="/updatePurchaseDatabase">
                                <template slot="title">
                                    <i class="el-icon-document"></i>
                                    <span>更新购买数据库</span>
                                </template>
                            </el-menu-item>

                            <el-menu-item index="/grabInfoFromWeb">
                                <template slot="title">
                                    <i class="el-icon-document"></i>
                                    <span>抓取航线信息</span>
                                </template>
                            </el-menu-item>

                            <el-menu-item index="/purchaseAircraft" disabled>购买飞机</el-menu-item>

                            <el-menu-item index="/autoConfirm" disabled>确认已完成订单</el-menu-item>

                        </el-menu-item-group>

                    </el-submenu>

                </el-menu>
            </el-aside>

            <!-- 右侧内容主体 -->
                <el-main>
                    <!-- 路由占位符 -->
                    <router-view></router-view>

                </el-main>
        </el-container>
    </el-container>
</template>

<script>
    export default {
        data() {
            return {
                UserNameX:'',


                // 是否折叠
                isCollapse: false,
                serverUrl: '127.0.0.1:9999',
                ws: null,
                test: '11111',
            }
        },
        mounted() {
            document.title = '主页';
            this.serverUrl = window.sessionStorage.getItem('serverUrl');
            this.UserNameX = window.sessionStorage.getItem('Username');
            
        },
        methods: {
            webSocketTest() {
                this.ws.send(JSON.stringify({ 'type': 'say', 'data': { 'content': '1000' } }));
                console.log('sent');

            },


            logout() {
                window.sessionStorage.clear(); // 清空token
                var sendData = { username: this.UserNameX };
                const result = this.$http.post('http://' + this.serverUrl + '/logOut', sendData).then(res => {
                    this.GLOBAL.wsModelPage = null;
                    this.GLOBAL.wsHubPage = null;
                    this.GLOBAL.wsModelPage = null;
                    this.GLOBAL.wsAutoPage = null;
                    this.GLOBAL.wsPlanningPage = null;
                    this.GLOBAL.wsDatabasePage = null;
                    this.GLOBAL.wsPersonalInfoPage = null;
                    this.$router.push('/login');
                    if (res.data.code == 200) return this.$message.warning(res.data.status);
                });
                 // 重定向到登录页
            },

            // 点击按钮，切换菜单的折叠与展开
            toggleCollapse() {
                this.isCollapse = !this.isCollapse
            },



        }
    };
</script>

<style lang="less" scoped>
    .home-container {
        height: 100%;
    }

    .el-header {
        background-color: #373D41;
        display: flex;
        justify-content: space-between;
        padding-left: 0;
        align-items: center;
        color: #fff;
        font-size: 25px;
        >div{
            display: flex;
            align-items: center;
            span{margin-left: 15px;}
        }
    }

    .el-aside {
        background-color: #333744;
        .el-menu{
            border-right: none;
            .el-submenu{
                           i{margin-right: 10px;
                             float: left;
                             transform:translate(0%,90%);
                            }
                            span{float: left;}
                       }
            .el-menu-item{
                i{margin-right: 15px;}
            }
        }
    }

    .el-main {
        background-color: #EAEDF1;
    }

    .toggle-button {
        background-color: #4A5064;
        font-size: 10px;
        line-height: 24px;
        color: #fff;
        text-align: center;
        letter-spacing: 0.2em;
        cursor: pointer;
    }
    .mainbox{
        width:70%;
    }

    
</style>