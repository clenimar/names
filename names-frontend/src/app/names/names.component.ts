import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-names',
  templateUrl: './names.component.html',
  styleUrls: ['./names.component.css']
})
export class NamesComponent implements OnInit {
  firstname;
  middlename;
  lastname;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.apiService.getFirstName().subscribe((firstname)=>{
      console.log(firstname);
      this.firstname = firstname['firstName'];
    });
    this.apiService.getMiddleName().subscribe((middlename)=>{
      console.log(middlename);
      this.middlename = middlename['middleName'];
    });
    this.apiService.getLastName().subscribe((lastname)=>{
      console.log(lastname);
      this.lastname = lastname['lastName'];
    });
  }

}
