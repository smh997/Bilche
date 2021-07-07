import { ModuleAccessor, Module } from 'vuex-module-accessor'

class RootState {
  hostname: string | undefined = undefined
}

class RootModule extends Module<RootState> {
  constructor() {
    super(RootState)
  }
}

export default new ModuleAccessor(new RootModule())
