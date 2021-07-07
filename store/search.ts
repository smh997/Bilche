// import Vue from 'vue'
import { ModuleAccessor, Module } from 'vuex-module-accessor'

// api
import { ApiApi, BasePlantList } from '~/api'
const api = new ApiApi()

class SearchState {
  pageSize: number = 9
  pageNumber: number = 0
  toxic?: boolean = undefined
  irritant?: boolean = undefined
  lifeSpan?: number = undefined
  pruning?: boolean = undefined
  fogging?: boolean = undefined
  cleaningPot?: boolean = undefined
  cleaningLeaves?: boolean = undefined
  category?: number[] = undefined
  search?: string = undefined
  plants: BasePlantList[] | undefined = undefined
}

export class SearchModule extends Module<SearchState> {
  constructor() {
    super(SearchState)
  }

  /**
   * Set & get of page number
   *
   * @memberof SearchModule
   */
  set pageNumber(pageNumber: number) {
    this.state.pageNumber = pageNumber
  }

  get pageNumber(): number {
    return this.state.pageNumber
  }

  /**
   * Set & get toxic
   *
   * @memberof SearchModule
   */
  set toxic(toxic: boolean | undefined) {
    this.state.toxic = toxic
  }

  get toxic(): boolean | undefined {
    return this.state.toxic
  }

  /**
   * Set & get irritant
   *
   * @memberof SearchModule
   */
  set irritant(irritant: boolean | undefined) {
    this.state.irritant = irritant
  }

  get irritant(): boolean | undefined {
    return this.state.irritant
  }

  /**
   * Set & get lifeSpan
   *
   * @memberof SearchModule
   */
  set lifeSpan(lifeSpan: number | undefined) {
    this.state.lifeSpan = lifeSpan
  }

  get lifeSpan(): number | undefined {
    return this.state.lifeSpan
  }

  /**
   * Set & get pruning
   *
   * @memberof SearchModule
   */
  set pruning(pruning: boolean | undefined) {
    this.state.pruning = pruning
  }

  get pruning(): boolean | undefined {
    return this.state.pruning
  }

  /**
   * Set & get fogging
   *
   * @memberof SearchModule
   */
  set fogging(fogging: boolean | undefined) {
    this.state.fogging = fogging
  }

  get fogging(): boolean | undefined {
    return this.state.fogging
  }

  /**
   * Set & get cleaningPot
   *
   * @memberof SearchModule
   */
  set cleaningPot(cleaningPot: boolean | undefined) {
    this.state.cleaningPot = cleaningPot
  }

  get cleaningPot(): boolean | undefined {
    return this.state.cleaningPot
  }

  /**
   * Set & get cleaningLeaves
   *
   * @memberof SearchModule
   */
  set cleaningLeaves(cleaningLeaves: boolean | undefined) {
    this.state.cleaningLeaves = cleaningLeaves
  }

  get cleaningLeaves(): boolean | undefined {
    return this.state.cleaningLeaves
  }

  /**
   * Set & get category
   *
   * @memberof SearchModule
   */
  set category(category: number[] | undefined) {
    this.state.category = category
  }

  get category(): number[] | undefined {
    return this.state.category
  }

  /**
   * Set & get plant
   *
   * @memberof SearchModule
   */
  set plants(plants: BasePlantList[] | undefined) {
    this.state.plants = plants
  }

  get plants(): BasePlantList[] | undefined {
    return this.state.plants
  }

  async searchPlants() {
    const result = await api.listBasePlants(
      this.state.pageSize,
      this.state.pageNumber,
      this.state.toxic,
      this.state.irritant,
      this.state.lifeSpan,
      this.state.pruning,
      this.state.fogging,
      this.state.cleaningPot,
      this.state.cleaningLeaves,
      this.state.search
      // [1, 2]
    )
    this.plants = result.data.results
  }
}

export default new ModuleAccessor(new SearchModule(), 'search/')
