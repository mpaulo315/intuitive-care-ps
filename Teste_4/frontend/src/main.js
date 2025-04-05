import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import 'primeicons/primeicons.css'
import {default as Theme} from "@primeuix/themes/aura" 

// Plugins
import PrimeVue from 'primevue/config'
import { VueQueryPlugin } from '@tanstack/vue-query'

const app = createApp(App)
app.use(PrimeVue, {
    theme: {
        preset: Theme,
    }
})
app.use(VueQueryPlugin)

app.mount('#app')