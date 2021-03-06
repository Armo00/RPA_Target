<template>
    <div>

        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>发票审核</el-breadcrumb-item>
        </el-breadcrumb>

        <!-- 卡片视图区域 -->
        <el-card class="box-card">
            <el-dialog title="修改"
                       :visible.sync="dialogVisibleFlag"
                       :before-close="placeholder"
                       width="30%">
                请仔细确认您的修改是否合法！
                <div>

                </div>


                <span slot="footer" class="dialog-footer">
                    <el-button @click="placeholder()">取 消</el-button>
                    <el-button type="primary" @click="placeholder()">确 定</el-button>
                </span>
            </el-dialog>

            <div class="fileBox">
                <el-form ref="form"
                         :model="ticketFormData">
                    <el-form-item></el-form-item>


                    <el-form-item v-for="(item, index) in fileData">
                        <el-button @click.prevent="setData(item)" style="width: 100%;"  >{{item.invoiceNo}}</el-button>
                    </el-form-item>

                </el-form>
            </div>

            <el-form ref="form"
                     :model="ticketFormData"
                     class="ticketForm"
                     label-width="120px">
                <el-form-item></el-form-item>
                <el-form-item label="境外发货人">
                    <el-col :span="6">
                        <el-input v-model="ticketFormData.overboardSender" style="width: 100%;"></el-input>
                    </el-col>
                    <el-col class="line" :span="2">发票号</el-col>
                    <el-col :span="6">
                        <el-input v-model="ticketFormData.invoiceNo" style="width: 100%;"></el-input>
                    </el-col>
                    <el-col class="line" :span="2">进口日期</el-col>
                    <el-col :span="6">
                        <el-date-picker type="date" placeholder="选择日期" v-model="ticketFormData.importDate" style="width: 100%;" value-format="yyyy-MM-dd"></el-date-picker>
                    </el-col>
                </el-form-item>

                <el-form-item label="销售指令号">
                    <el-col :span="6">
                        <el-input v-model="ticketFormData.salesOrderNo" style="width: 100%;"></el-input>
                    </el-col>
                    <el-col class="line" :span="2">成交方式</el-col>
                    <el-col :span="6">
                        <el-input v-model="ticketFormData.incoterms" style="width: 100%;"></el-input>
                    </el-col>

                </el-form-item>

                <el-form-item label="起运国信息">
                    <el-input type="textarea" v-model="ticketFormData.fromAddress" :rows="4"></el-input>
                </el-form-item>
                <el-form-item label="最终仓库">
                    <el-input type="textarea" v-model="ticketFormData.toAddress" :rows="4"></el-input>
                </el-form-item>

                <el-form-item v-for="(item, index) in ticketFormData.importItems"
                              :label="'进口货物' + index">
                    <el-input v-model="item.materialDescription" placeholder="料号" class="cargoInput" id="md1"></el-input>
                    <el-input v-model="item.ogCountry" placeholder="原产国" class="cargoInput"></el-input>
                    <el-input v-model="item.HSTNumber" placeholder="HS归类参考" class="cargoInput"></el-input>
                    <el-input v-model="item.quantity" placeholder="数量" class="cargoInput"></el-input>
                    <el-input v-model="item.unitPrice" placeholder="单价" class="cargoInput"></el-input>
                    <el-input v-model="item.extendedPrice" placeholder="单个料号总价" class="cargoInput"></el-input>
                    <el-input v-model="item.ECCN" placeholder="出口管制分类号码" class="cargoInput"></el-input>
                    <el-input v-model="item.license" placeholder="许可证" class="cargoInput"></el-input>
                    <el-date-picker type="date" placeholder="有效期" v-model="item.valid" class="cargoInput" value-format="yyyy-MM-dd"></el-date-picker>

                    <el-button @click.prevent="removeItem(item)" type="danger" round>删除</el-button>
                </el-form-item>
                <el-form-item>
                    <el-button @click="addItem" name="newItem">新增货物</el-button>
                    <el-button type="primary" @click="getData()" name="commitItem">提交</el-button>
                </el-form-item>

            </el-form>





        </el-card>

    </div>
</template>

<script>
    export default {
        mounted() {
            this.serverUrl = window.sessionStorage.getItem('serverUrl'); 
            this.getData();
        },
        data() {
            return {
                serverUrl: '127.0.0.1:9999',

                allHub: [],
                awaitingPurchaseList: [],

                multipleSelection: [],
                dialogVisibleFlag: false,

                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                },
                ticketFormData: {
                    overboardSender: '',
                    fromAddress: '',
                    toAddress: '',
                    invoiceNo: '',
                    importDate:'',
                    salesOrderNo: '',
                    incoterms: '',
                    importItems: [
                        { materialDescription: '', ogCountry: '', HTSNumber: '', quantity: '', unitPrice: '', extendedPrice: '', ECCN: '', license: '', valid: '' },
                    ],
                    
                },
                fileData:[],
            }
        },
        methods: {
           

            handleSelectionChange(val) {
                this.multipleSelection = val;
            },
            placeholder() {
                console.log('rua');
            },
            removeItem(item) {
                var index = this.ticketFormData.importItems.indexOf(item)
                if (index !== -1) {
                    this.ticketFormData.importItems.splice(index, 1)
                };
            },
            addItem() {
                var item = { materialDescription: '', ogCountry: '', HSTNumber: '', quantity: '', unitPrice: '', extendedPrice: '', ECCN: '', license: '', valid: '' };
                this.ticketFormData.importItems.push(item);
            },

            getData() {
                var sendData = { mode: 'awaitingAuditTicket' };
                const result = this.$http.post('http://' + this.serverUrl + '/getData', sendData).then(res => {
                    console.log(res.data.data);
                    this.fileData = res.data.data;
                });
            },
            setData(item) {
                
                this.ticketFormData = item;
            },




            commitTicketData() {
                var sendData = { data: this.ticketFormData, mode:'awaitingAuditTicket' };
                console.log(this.ticketFormData);
                const result = this.$http.post('http://' + this.serverUrl + '/commitData', sendData).then(res => {
                    console.log(res.data);
                    
                    
                });
            },
            


        }

    }
</script>

<style lang="less" scoped>

   
    .button {
        margin-left: 20px;
        
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
    .ticketForm {
        border: 2px solid #333744;
        width: 70%;
        display:inline-block;
    }
    .fileBox {
        width: 28%;
        display:inline-block;
        border: 2px solid #333744;
        margin-right:10px;
        vertical-align:top;
    }
    .inline-input {
        margin-left: 10px;
        width: 40%;
        float:left;
    }
    .cargoInput{
        width:15%;
        float:left;
        margin-right:10px;
    }

</style>