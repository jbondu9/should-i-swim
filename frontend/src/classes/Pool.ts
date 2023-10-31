import { ApiPool } from "../interfaces/ApiPool";

export class Pool {
  id: number;
  poolName: string;
  swimmingPoolName: string;

  isOpened: boolean;
  currentCapacity: number;
  maximumCapacity: number;

  updatedAt: Date;

  constructor(pool?: ApiPool) {
    this.id = pool?._id ?? 0;
    this.poolName = pool?.pool_name ?? "";
    this.swimmingPoolName = pool?.swimming_pool_name ?? "";

    this.isOpened = pool?.is_opened ?? false;
    this.currentCapacity = pool?.current_capacity ?? 0;
    this.maximumCapacity = pool?.maximum_capacity ?? 0;

    this.updatedAt = pool?.updated_at ? new Date(pool.updated_at) : new Date();
  }
}
