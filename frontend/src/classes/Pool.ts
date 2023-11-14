import { ApiPool } from "../interfaces/ApiPool";

export class Pool {
  id: number;
  swimmingPool: string;
  basin: string;

  isOpened: boolean;
  currentCapacity: number;
  maximumCapacity: number;

  updatedAt: Date;

  constructor(pool?: ApiPool) {
    this.id = pool?._id ?? 0;
    this.swimmingPool = pool?.swimming_pool ?? "";
    this.basin = pool?.basin ?? "";

    this.isOpened = pool?.is_opened ?? false;
    this.currentCapacity = pool?.current_capacity ?? 0;
    this.maximumCapacity = pool?.maximum_capacity ?? 0;

    this.updatedAt = pool?.updated_at ? new Date(pool.updated_at) : new Date();
  }
}
