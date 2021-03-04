<template>
    <div>

        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>发票填报</el-breadcrumb-item>
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
                        <el-date-picker type="date" placeholder="选择日期" v-model="ticketFormData.importDate" style="width: 100%;"></el-date-picker>
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

                <el-form-item label="活动区域">
                    <el-select v-model="form.region" placeholder="请选择活动区域">
                        <el-option label="区域一" value="shanghai"></el-option>
                        <el-option label="区域二" value="beijing"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="活动时间">
                    <el-col :span="11">
                        <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
                    </el-col>
                    <el-col class="line" :span="2">-</el-col>
                    <el-col :span="11">
                        <el-time-picker placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
                    </el-col>
                </el-form-item>
                <el-form-item label="即时配送">
                    <el-switch v-model="form.delivery"></el-switch>
                </el-form-item>
                <el-form-item label="活动性质">
                    <el-checkbox-group v-model="form.type">
                        <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
                        <el-checkbox label="地推活动" name="type"></el-checkbox>
                        <el-checkbox label="线下主题活动" name="type"></el-checkbox>
                        <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
                    </el-checkbox-group>
                </el-form-item>
                <el-form-item label="特殊资源">
                    <el-radio-group v-model="form.resource">
                        <el-radio label="线上品牌商赞助"></el-radio>
                        <el-radio label="线下场地免费"></el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="活动形式">
                    <el-input type="textarea" v-model="form.desc"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary">立即创建</el-button>
                    <el-button>取消</el-button>
                </el-form-item>
            </el-form>




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
                    
                },
            }
        },
        methods: {
           

            handleSelectionChange(val) {
                this.multipleSelection = val;
            },
            placeholder() {
                console.log('rua');
            }
            


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
        width: 100%;
    }
    .inline-input {
        margin-left: 10px;
        width: 40%;
        float:left;
    }

</style>