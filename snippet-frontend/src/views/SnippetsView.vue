<template>
    <main class="container">
        <h1 class="title is-1">Snippets</h1>
        <p class="subtitle">List of your current snippets</p>
        <div class="columns is-multiline">
            <div class="column is-4" v-for="snippet in snippets" :key="snippet.id">
                <div class="card">
                    <div class="card-content">
                        <div class="content">
                            <h2 class="title is-4">{{ snippet.name }}</h2>
                            <p>{{ snippet.description }}</p>
                            <pre><code>{{ snippet.code }}</code></pre>
                        </div>
                    </div>
                    <footer class="card-footer">
                        <p>Pendiente</p>
                    </footer>
                </div>
            </div>
        </div>
    </main>
</template>

<script lang="ts">
import { defineComponent, nextTick, onMounted, ref } from 'vue';
import { API_BASE_URL } from '@/config';
import type { Snippet } from '@/types/Snippet'; 
import hljs from 'highlight.js';
import 'highlight.js/styles/atom-one-dark.css';

export default defineComponent({
    name: 'SnippetsView',
    setup() {
        const snippets = ref<Snippet[]>([]);

        onMounted(() => {
            fetch(`${API_BASE_URL}/snippets`)
                .then(response => response.json())
                .then((sn: Snippet[]) => {
                    snippets.value = sn;
                    nextTick(() => {
                        document.querySelectorAll('pre code').forEach((block) => {
                            hljs.highlightBlock(block as HTMLElement);
                        });
                    });
                });
        });

        return {
            snippets,
        };
    },
});
</script>

<style scoped>
pre {
    overflow-x: auto;
}
</style>