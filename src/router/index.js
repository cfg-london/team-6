import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Search from '@/components/Search'
import Discover from '@/components/Discover'
import Laureates from '@/components/Laureates'
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
      path: 'nominations',

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
    },
    {
      path: '/discover',
      name: 'Discover',
      component: Discover
    }, 
    {
      path: '/laureates',
      name: 'Laureates',
      component: Laureates
    }
  ]
})