<template>
    <div>

        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>更新购买数据库</el-breadcrumb-item>
        </el-breadcrumb>

        <!-- 卡片视图区域 -->
        <el-card class="box-card">
            <el-dialog title="修改"
                       :visible.sync="dialogVisibleFlag"
                       :before-close="resetModelDatabaseForm"
                       width="30%">
                请仔细确认您的修改是否合法！
                <div>
                    <el-tag class="dialog-item">机型:</el-tag>
                    <el-input class="dialog-input" v-model="modelDatabaseForm.model" prefix-icon="el-icon-s-tools" placeholder="机型"></el-input>
                    <el-tag class="dialog-item">hub:</el-tag>
                    <el-input class="dialog-input" v-model="modelDatabaseForm.hub" prefix-icon="el-icon-s-home" placeholder="hub"></el-input>
                    <el-tag class="dialog-item">航线:</el-tag>
                    <el-input class="dialog-input" v-model="modelDatabaseForm.line" prefix-icon="el-icon-s-promotion" placeholder="航线"></el-input>
                    <el-tag class="dialog-item">经济舱:</el-tag>
                    <el-input class="dialog-input" v-model="modelDatabaseForm.eco" prefix-icon="el-icon-user" placeholder="经济舱"></el-input>
                    <el-tag class="dialog-item">公务舱:</el-tag>
                    <el-input class="dialog-input" v-model="modelDatabaseForm.bus" prefix-icon="el-icon-user-solid" placeholder="公务舱"></el-input>
                    <el-tag class="dialog-item">头等舱:</el-tag>
                    <el-input class="dialog-input" v-model="modelDatabaseForm.first" prefix-icon="el-icon-s-custom" placeholder="头等舱"></el-input>
                    <el-tag class="dialog-item">货仓:</el-tag>
                    <el-input class="dialog-input" v-model="modelDatabaseForm.payload" prefix-icon="el-icon-goods" placeholder="货舱"></el-input>
                    <el-tag class="dialog-item">数量:</el-tag>
                    <el-input class="dialog-input" v-model="modelDatabaseForm.quantity" prefix-icon="el-icon-s-help" placeholder="数量"></el-input>
                </div>


                <span slot="footer" class="dialog-footer">
                    <el-button @click="resetModelDatabaseForm()">取 消</el-button>
                    <el-button type="primary" @click="editDatabaseContentConfirmed()">确 定</el-button>
                </span>
            </el-dialog>



            <div class="searchBox">
                <el-form label-width="0px">
                    <!--新增数据项-->
                    <el-form-item label="">
                        <div>新增数据项</div>
                        <el-tag class="dialog-item">机型:</el-tag>
                        <el-input class="dialog-input" v-model="modelDatabaseForm.model" prefix-icon="el-icon-s-tools" placeholder="机型"></el-input>
                        <el-tag class="dialog-item">hub:</el-tag>
                        <el-input class="dialog-input" v-model="modelDatabaseForm.hub" prefix-icon="el-icon-s-home" placeholder="hub"></el-input>
                        <el-tag class="dialog-item">航线:</el-tag>
                        <el-input class="dialog-input" v-model="modelDatabaseForm.line" prefix-icon="el-icon-s-promotion" placeholder="航线"></el-input>
                        <el-tag class="dialog-item">经济舱:</el-tag>
                        <el-input class="dialog-input" v-model="modelDatabaseForm.eco" prefix-icon="el-icon-user" placeholder="经济舱"></el-input>
                        <el-tag class="dialog-item">公务舱:</el-tag>
                        <el-input class="dialog-input" v-model="modelDatabaseForm.bus" prefix-icon="el-icon-user-solid" placeholder="公务舱"></el-input>
                        <el-tag class="dialog-item">头等舱:</el-tag>
                        <el-input class="dialog-input" v-model="modelDatabaseForm.first" prefix-icon="el-icon-s-custom" placeholder="头等舱"></el-input>
                        <el-tag class="dialog-item">货仓:</el-tag>
                        <el-input class="dialog-input" v-model="modelDatabaseForm.payload" prefix-icon="el-icon-goods" placeholder="货舱"></el-input>
                        <el-tag class="dialog-item">数量:</el-tag>
                        <el-input class="dialog-input" v-model="modelDatabaseForm.quantity" prefix-icon="el-icon-s-help" placeholder="数量"></el-input>
                    </el-form-item>

                    <el-form-item label="">
                        <el-button  @click="resetModelDatabaseForm()" class="button">重置</el-button>
                        <el-button type="primary" @click="confirmAddData()" class="button">确认</el-button>
                    </el-form-item>
                    <el-form-item class="confirmBox"></el-form-item>


                    <el-form-item label="">
                        <el-button type="primary" @click="commitDataModification()" class="button">递交数据</el-button>
                    </el-form-item>




                </el-form>
            </div>
            <div class="modifyList">
                <el-table :data="awaitingPurchaseList"
                          ref="multipleTable"
                          @selection-change="handleSelectionChange"
                          border
                          height="800"
                          style="width: 100%">
                    <el-table-column type="selection"
                                     min-width="20px">
                    </el-table-column>
                    <el-table-column prop="model"
                                     label="机型"
                                     sortable
                                     min-width="60px">
                    </el-table-column>

                    <el-table-column prop="hub"
                                     label="hub"
                                     sortable
                                     min-width="30px">
                    </el-table-column>
                    <el-table-column prop="line"
                                     label="航线"
                                     min-width="30px">
                    </el-table-column>
                    <el-table-column prop="seat2"
                                     label="构型"
                                     sortable
                                     min-width="60px">
                    </el-table-column>
                    <el-table-column prop="num"
                                     label="数量"
                                     sortable
                                     min-width="20px">
                    </el-table-column>
                    <el-table-column prop="order"
                                     label="操作"
                                     min-width="40px">
                        <template slot-scope="scope">
                            <el-button type="primary" @click="editDatabaseContent(scope.row)" icon="el-icon-edit"   circle></el-button>
                            <el-button type="danger"  @click="deleteFromDatabase(scope.row)"  icon="el-icon-delete" circle></el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </div>


        </el-card>

    </div>
</template>

<script>
    export default {
        mounted() {
            this.serverUrl = window.sessionStorage.getItem('serverUrl');           
        },
        data() {
            return {
                serverUrl: '127.0.0.1:9999',

                allHub: [],
                awaitingPurchaseList: [],

                multipleSelection: [],
                dialogVisibleFlag: false,
                modelDatabaseForm: {model:'',hub:'',line:'',eco:'',bus:'',first:'',payload:'',quantity:'',indexID:-1},
            }
        },
        methods: {
           

            handleSelectionChange(val) {
                this.multipleSelection = val;
            },
            commitDataModification() {
                //console.log(this.awaitingPurchaseList);
                var sendData = { username: window.sessionStorage.getItem('Username'), data: this.awaitingPurchaseList ,mode:'override'};
                const result = this.$http.post('http://' + this.serverUrl + '/commitDataModification', sendData).then(res => {
                    if (res.data.return_code == 9000) return this.$message.error(res.data.result);
                    //console.log(res.data);
                });

            },

            confirmAddData() {
                var item = {
                    model: this.modelDatabaseForm.model,
                    hub: this.modelDatabaseForm.hub,
                    line: this.modelDatabaseForm.line,
                    eco: this.modelDatabaseForm.eco,
                    bus: this.modelDatabaseForm.bus,
                    first: this.modelDatabaseForm.first,
                    cargo: this.modelDatabaseForm.payload,
                    num: this.modelDatabaseForm.quantity,
                    status: '待处理',
                    seat2: '(' + this.modelDatabaseForm.eco + '/' + this.modelDatabaseForm.bus + '/' + this.modelDatabaseForm.first + '/' + this.modelDatabaseForm.payload + ')',
                };
                //console.log(this.awaitingPurchaseList[0]);
                this.awaitingPurchaseList.push(item);
            },
            resetModelDatabaseForm() {
                this.modelDatabaseForm = { model: '', hub: '', line: '', eco: '', bus: '', first: '', payload: '', quantity: '', indexID: -1 };
                this.dialogVisibleFlag = false;
            },

            editDatabaseContent(item) {
                this.dialogVisibleFlag = true;
                //console.log(item);
                this.modelDatabaseForm.model = item.model;
                this.modelDatabaseForm.hub = item.hub;
                this.modelDatabaseForm.line = item.line;
                this.modelDatabaseForm.eco = item.eco;
                this.modelDatabaseForm.bus = item.bus;
                this.modelDatabaseForm.first = item.first;
                this.modelDatabaseForm.payload = item.cargo;
                this.modelDatabaseForm.quantity = item.num;
                this.modelDatabaseForm.indexID = this.awaitingPurchaseList.indexOf(item);
            },

            editDatabaseContentConfirmed() {
                var item = this.modelDatabaseForm.indexID;
                this.awaitingPurchaseList[item].model = this.modelDatabaseForm.model;
                this.awaitingPurchaseList[item].hub = this.modelDatabaseForm.hub;
                this.awaitingPurchaseList[item].line = this.modelDatabaseForm.line;
                this.awaitingPurchaseList[item].eco = this.modelDatabaseForm.eco;
                this.awaitingPurchaseList[item].bus = this.modelDatabaseForm.bus;
                this.awaitingPurchaseList[item].first = this.modelDatabaseForm.first;
                this.awaitingPurchaseList[item].cargo = this.modelDatabaseForm.payload;
                this.awaitingPurchaseList[item].num = this.modelDatabaseForm.quantity;
                var temp = '(' + this.modelDatabaseForm.eco + '/' + this.modelDatabaseForm.bus + '/' + this.modelDatabaseForm.first + '/' + this.modelDatabaseForm.payload + ')';
                this.awaitingPurchaseList[item].seat2 = temp;
                this.resetModelDatabaseForm();
            },
            deleteFromDatabase(item) {
                var index = this.awaitingPurchaseList.indexOf(item);
                this.$confirm('您确定要删除这项内容么？', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    if (index !== -1) {
                        this.awaitingPurchaseList.splice(index, 1);
                    };
                }).catch(() => {
                });


                
            },
            getPurchaseDataInfo() {
                var sendData = {username: window.sessionStorage.getItem('Username') };
                const result = this.$http.post('http://' + this.serverUrl + '/getPurchaseDataInfo', sendData).then(res => {
                    if (res.data.return_code == 9000) return this.$message.error(res.data.result);
                    var item;
                    this.awaitingPurchaseList = [];
                    for (item in res.data) {
                        var temp = res.data[item];
                        this.awaitingPurchaseList.push(temp);
                    };
                });
            },


        }

    }
</script>

<style lang="less" scoped>
    .progressBar {
        height: 80px;
        width: 90%;
        transform: translate(0%,20%);
        margin-left: 20px;
    }
    .tag1 {
        height: 50px;
        width: 100%;
        font-size: 220%;
        text-shadow: 0 0 3px #ddd;
        font-family: DengXian;
    }
    .tag1Word {
        transform: translate(35%,30%);
    }
    .searchBox {
        vertical-align:top;
        border: 3px solid #333744;
        width: 20%;

        display:inline-block;
        transform: translate(0%,0%);
    }


    .modifyList {
        vertical-align: top;
        display: inline-block;
        border: 3px solid #333744;
        width: 78%;
        height: 800px;
        transform: translate(1%,0%);
    }
    .button {
        margin-left: 20px;
        
    }
    .inline-input {
        margin-left: 10px;
        width: 60%;
        transform: translate(-0%,0%);
    }
    .dialog-input {
        margin-left: 10px;
        width: 60%;
    }
    .dialog-item{
        width:30%;
    }
    .confirmBox {
        border: 2px solid #333744;
        width:99.5%;
        transform:translate(-0%,0%);
    }

</style>