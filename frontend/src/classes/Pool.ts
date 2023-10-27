import { ApiPool } from "../interfaces/ApiPool";

export class Pool {
  id: number;
  poolName: string;
  swimmingPoolName: string;

  open: boolean;
  currentCapacity: number;
  maximumCapacity: number;
  updatedAt: Date;

  constructor(pool?: ApiPool) {
    this.id = pool?._id ?? 0;
    this.poolName = pool?.pool_name ?? "";
    this.swimmingPoolName = pool?.swimming_pool_name ?? "";

    this.open = pool?.open ?? false;
    this.currentCapacity = pool?.current_capacity ?? 0;
    this.maximumCapacity = pool?.maximum_capacity ?? 0;
    this.updatedAt = pool?.updated_at ?? new Date();
  }
}
