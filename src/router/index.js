import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/home.vue'
import Login from '../components/Login.vue'

import UpdateDatabase from '../components/updateDatabase.vue'
import Filling from '../components/fillingPage.vue'
import AuditTicket from '../components/auditTicket.vue'

import { Message } from 'element-ui';
import axios from "axios"
axios.defaults.headers.post['Content-Type'] = 'text/plain'

Vue.use(VueRouter)

const routes = [
    { path: '/', redirect: '/login' },
    {
        path: '/home', component: Home, title: '��ҳ', children: [
            { path: '/updatePurchaseDatabase', component: UpdateDatabase },
            { path: '/fillingTicket', component: Filling },
            { path: '/auditTicket', component: AuditTicket },
        ]
    },
    { path: '/login', component: Login, title: '��¼' },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

//����·������  load router guard
router.beforeEach((to, from, next) => {

    if (to.path === '/login') return next();
    //��ȡtoken get token
    const tokenStr = window.sessionStorage.getItem('token');
    var serverUrl = window.sessionStorage.getItem('serverUrl');

    if (!tokenStr) {
        return next('/login');
    };
    if (to.path == '/home') {
        var sendData = { username: window.sessionStorage.getItem('Username'), token: tokenStr };
        axios.post('http://' + serverUrl + '/checkToken', JSON.stringify(sendData)).then(res => {
            console.log(res);
            if (res.data.return_code == 200) { next() }
            else {
                Vue.use(Message.error('You Do Not Have The Authority To Access This Page'));
                next('/login');
            };
        }).catch(function (error) {
            console.log(error);
        });

    }
    next();
})

export default router
