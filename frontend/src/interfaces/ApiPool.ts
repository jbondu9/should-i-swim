export interface ApiPool {
  _id: number;
  pool_name: string;
  swimming_pool_name: string;

  open: boolean;
  current_capacity: number;
  maximum_capacity: number;
  updated_at: Date;
}
