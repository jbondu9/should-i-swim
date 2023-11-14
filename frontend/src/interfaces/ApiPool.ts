export interface ApiPool {
  _id: number;
  swimming_pool: string;
  basin: string;

  is_opened: boolean;
  current_capacity: number;
  maximum_capacity: number;

  updated_at: Date;
}
