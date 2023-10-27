import { Answer } from "../enums/Answer";
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

  shouldISwim(): Answer {
    if (!this.open) {
      return Answer.Closed;
    }

    const occupancyRate =
      this.maximumCapacity > 0
        ? (this.currentCapacity / this.maximumCapacity) * 100
        : 0;

    if (0 < occupancyRate && occupancyRate <= 15) {
      return Answer.NearlyEmpty;
    } else if (15 < occupancyRate && occupancyRate <= 35) {
      return Answer.FewPeople;
    } else if (35 < occupancyRate && occupancyRate <= 65) {
      return Answer.HalfFull;
    } else if (65 < occupancyRate && occupancyRate <= 90) {
      return Answer.Crowed;
    }

    return Answer.No;
  }
}
