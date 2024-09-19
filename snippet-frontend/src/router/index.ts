import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SnippetsView from '@/views/SnippetsView.vue'
import AddView from '@/views/AddView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/snippets',
      name: 'snippets',
      component: SnippetsView
    },
    {
      path: '/add',
      name: 'add',
      component: AddView
    }
  ]
})

export default router
