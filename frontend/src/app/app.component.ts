import { NgFor } from "@angular/common";
import { Component } from "@angular/core";
import { RouterLink, RouterLinkActive, RouterOutlet } from "@angular/router";

@Component({
  selector: "app-root",
  standalone: true,
  imports: [NgFor, RouterLink, RouterLinkActive, RouterOutlet],
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"],
})
export class AppComponent {
  navigation = [
    { path: "", label: "Dashboard" },
    { path: "issue-atlas", label: "Issue Atlas" },
    { path: "mechanic-signal-hub", label: "Mechanic Signal Hub" },
    { path: "design-impact", label: "Design Impact Simulator" },
    { path: "supplier-integrity", label: "Supplier Integrity" },
    { path: "assembly-guidance", label: "Assembly Guidance" },
    { path: "change-feedback", label: "Change Feedback Loop" },
  ];
}
