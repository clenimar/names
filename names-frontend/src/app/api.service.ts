import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient: HttpClient) { }

  public getFirstName(){
    return this.httpClient.get("http://localhost:5001/user/1/firstname");
  }

  public getMiddleName(){
    return this.httpClient.get("http://localhost:5001/user/1/middlename");
  }

  public getLastName(){
    return this.httpClient.get("http://localhost:5001/user/1/lastname");
  }
}
