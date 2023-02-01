import axios from "axios"
import { defineStore } from 'pinia'
import { isEmpty } from 'lodash';
import { server } from '../helper';

interface ScatterPoint extends Point{
    cluster: string;
}


export const createStore = defineStore('App', {
	state: () => ({
        wordCount: [] as ScatterPoint[],
        size: { width: 0, height: 0 } as ComponentSize,
        margin: { left: 20, right: 20, top: 20, bottom: 40 } as Margin,
        methods: ['PCA', 't-SNE'] as string[],
        selectedMethod: 'PCA', // default value
    }),
    getters: {
        resize: (state) => {
            return (!isEmpty(state.points) && state.size)
        }
    },
    actions: {
        async fetchExample(method: string) { // same API request but in slightly different syntax when it's declared as a method in a component or an action in the store.
            axios.post(`${server}/fetchExample`, {method: method})
                .then(resp => {
                    this.wordCount = resp.data.wordCount;
                    return true;
                })
                .catch(error => console.log(error));
        },
    }
})