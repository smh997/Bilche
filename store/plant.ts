// import Vue from 'vue'
import { ModuleAccessor, Module } from 'vuex-module-accessor'

// api
import { ApiApi, BasePlantObject } from '~/api'

const api = new ApiApi()

class PlantState {
  plant: BasePlantObject | undefined = undefined
}

export class PlantModule extends Module<PlantState> {
  constructor() {
    super(PlantState)
  }

  /**
   * Set & get plant info
   *
   * @memberof PlantModule
   */
  set plant(plant: BasePlantObject | undefined) {
    this.state.plant = plant
  }

  get plant(): BasePlantObject | undefined {
    return this.state.plant
  }

  async getPlant(plantId: string) {
    const result = await api.retrieveBasePlant(Number(plantId))
    this.plant = result.data
  }
}

export default new ModuleAccessor(new PlantModule(), 'plant/')
