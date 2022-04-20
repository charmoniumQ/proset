{
  description = "Flake utils demo";
  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        name = "proset";
      in {
        devShell = pkgs.mkShell {
          buildInputs = [
            (pkgs.python39.withPackages(ps: with ps; [svgwrite]))
            pkgs.pdftk
	    pkgs.librsvg
          ];
	  shellHook = ''
	    export PREPEND_TO_PS1="(${name}) "
	  '';
        };
      }
    );
}
