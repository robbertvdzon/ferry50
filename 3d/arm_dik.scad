

difference(){
	union(){

        translate([15,-5,0]){
            cube([8,13,10], center=false);
        }         

        translate([0,-5,0]){
            cube([15,3,10], center=false);
        }         
        translate([0,5,0]){
            cube([15,3,10], center=false);
        }         

	}
	union() {
        translate([3,15,5]){
            rotate([90,0,0]){
                cylinder(h=117, r=1.5, $fn=100, center=false);
            }
        }         
        translate([0,1.5,5]){
            rotate([0,90,0]){
                cylinder(h=117, r=2.2, $fn=100, center=false);
            }
        }         

        
	}
}
