import axios from "axios"
import { defineStore } from 'pinia'
import { isEmpty } from 'lodash';
import { server } from '../helper';

export const createStore = defineStore('App', {
	state: () => ({
        wordCount: [] as string[],
    }),
    getters: {
        resize: (state) => {
            return (!isEmpty(state.points) && state.size)
        }
    },
    actions: {
        async fetchExample(method: string) { // same API request but in slightly different syntax when it's declared as a method in a component or an action in the store.
            axios.post(`${server}/fetchExample`)
                .then(resp => {
                    this.wordCount = resp.data.wordCount;
                    console.log(this.wordCount);
                    return true;
                })
                .catch(error => console.log(error));
        },
    }
})