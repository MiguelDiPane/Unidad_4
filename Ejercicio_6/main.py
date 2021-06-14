from claseRepositorioProvincias import RespositorioProvincias
from vistasProvincias import ProvinciasView
from claseControladorProvincias import ControladorProvincias
from claseObjectEncoder import ObjectEncoder

def main():
    conn=ObjectEncoder('provincias.json')
    repo=RespositorioProvincias(conn)
    vista=ProvinciasView()
    ctrl=ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()