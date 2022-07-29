         require([
            "jquery",
            "splunkjs/mvc/searchmanager",
            "splunkjs/mvc/simplexml/ready!"
          ], function(
              $,
              SearchManager
          ) {
              var mysearch = new SearchManager({
                  id: "mysearch",
                  autostart: "false",
                  search: "|makeresults| outputlookup myfile" 
              });
              $(".button1").on("click", function (){
                  var ok = confirm("Are you sure?");
                  if (ok){
                      mysearch.startSearch();
                      alert('attempted restart!');
                  } //else {
                  //    alert('user did not click ok!');
                  //}
              });
         });
