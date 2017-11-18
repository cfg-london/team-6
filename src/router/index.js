import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Search from '@/components/Search'
import 'vue-material-design-icons/styles.css'

import Article from '@/components/Article'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: 'nobel_prizes',

    },
    {
      path: 'nomination',

    },
    {
      path: 'ceremonies',
    },
    {
      path: 'alfred_nobel'
    },
    {
      path: 'educational'
    },
    {
      path: 'events'
    },
    {
      path: '/search',
      component: Search
    },
    {
      path: '/article',
      name: 'Article',
      component: Article
    }
  ]
})
