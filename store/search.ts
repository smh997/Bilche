// import Vue from 'vue'
import { ModuleAccessor, Module } from 'vuex-module-accessor'

class SearchState {
  comment: string | undefined = undefined
}

export class SearchModule extends Module<SearchState> {
  constructor() {
    super(SearchState)
  }

  set comment(comment: string | undefined) {
    this.state.comment = comment
  }

  get comment(): string | undefined {
    return this.state.comment
  }
}

export default new ModuleAccessor(new SearchModule(), 'search/')
