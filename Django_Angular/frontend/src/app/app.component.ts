import { Component, ViewChild } from '@angular/core';

import { JsonEditorComponent, JsonEditorOptions } from 'ang-jsoneditor';
import { schema } from './schema.value';

import { FetchServer } from './server.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent{

  @ViewChild(JsonEditorComponent) editor: JsonEditorComponent;

  options = new JsonEditorOptions();
  data = schema;
  receive = {};
  disableBtn = true;
  isDisplay = true;

  constructor(private _service: FetchServer) {
    this.options.mode = 'code';
    this.options.modes = ['code', 'text', 'tree', 'view'];
    // this.options.schema = schema;
    this.options.statusBar = false;
    this.options.onChange = () => this.fetchdata()
  }

  fetchdata() {
    try {
      this.disableBtn = true;
      console.log(this.editor.get());
    } catch(e) {
      this.disableBtn = false;
    }
  }

  getServerData() {
    try {
      this._service.getFakerData(this.editor.get()).subscribe(data => this.displayData(data));
    } catch(e) {
      alert('Data validation Failed.')
    }
  }

  displayData(data) {
    this.isDisplay = false;
    this.receive = data;
  }
}
