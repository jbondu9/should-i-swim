import { ApiAnswer } from "../interfaces/ApiAnswer";

export class Answer {
  reasonName: string;
  reasonDescription: string;

  constructor(answer?: ApiAnswer) {
    this.reasonName = answer?.reason_name ?? "";
    this.reasonDescription = answer?.reason_description ?? "";
  }
}
