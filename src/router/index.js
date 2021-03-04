import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/home.vue'
import Login from '../components/Login.vue'

import UpdateDatabase from '../components/updateDatabase.vue'
import Filling from '../components/fillingPage.vue'

Vue.use(VueRouter)

const routes = [
    { path: '/', redirect: '/login' },
    {
        path: '/home', component: Home, title: 'Ö÷Ò³', children: [
            { path: '/updatePurchaseDatabase', component: UpdateDatabase },
            { path: '/filling', component: Filling },
        ]
    },
    { path: '/login', component: Login, title: 'µÇÂ¼' },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
