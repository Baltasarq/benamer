# benamer tests (c) Baltasar 2021 MIT License <baltasarq@gmail.com>


import unittest
import benamer


class TestFunctionalities(unittest.TestCase):
    def setUp(self):
        self.fns = [
            "benamer.py",
            "img_123456.jpg",
            "img_987654.jpg",
            "doc_peticion.doc",
            "notas.TXT"
            ]
        self.args = {"verbose": False, "sort": False, "print": False}
    
    def test_remove_prefix(self):
        file_sust_result = [
            "benamer.py",
            "123456.jpg",
            "987654.jpg",
            "doc_peticion.doc",
            "notas.TXT"
            ]
        
        self.args["remove_prefix"] = "img_"
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_remove_suffix(self):
        file_sust_result = [
            "benam.py",
            "img_123456.jpg",
            "img_987654.jpg",
            "doc_peticion.doc",
            "notas.TXT"
            ]
        
        self.args["remove_suffix"] = "er"
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_add_suffix(self):
        file_sust_result = [
            "benamer-origa.py",
            "img_123456-origa.jpg",
            "img_987654-origa.jpg",
            "doc_peticion-origa.doc",
            "notas-origa.TXT"
            ]
        
        self.args["add_suffix"] = "-origa"
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_add_prefix(self):
        file_sust_result = [
            "aa-benamer.py",
            "aa-img_123456.jpg",
            "aa-img_987654.jpg",
            "aa-doc_peticion.doc",
            "aa-notas.TXT"
            ]
        
        self.args["add_prefix"] = "aa-"
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_sust(self):
        file_sust_result = [
            "benaker.py",
            "ikg_123456.jpg",
            "ikg_987654.jpg",
            "doc_peticion.doc",
            "notas.TXT"
            ]
        
        self.args["sust"] = "m/k"
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_sust_whole(self):
        file_sust_result = [
            "kk.py",
            "kk.jpg",
            "kk.jpg",
            "kk.doc",
            "kk.TXT"
            ]
        
        self.args["sust"] = "/kk"
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_sust_nothing(self):
        file_sust_result = [
            "benamer.py",
            "123456.jpg",
            "987654.jpg",
            "doc_peticion.doc",
            "notas.TXT"
            ]
        
        self.args["sust"] = "img_/"
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_add_count(self):
        file_sust_result = [
            "benamer11.py",
            "img_12345612.jpg",
            "img_98765413.jpg",
            "doc_peticion14.doc",
            "notas15.TXT"
            ]
        
        self.args["add_count"] = 11
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_mins(self):
        file_sust_result = [
            "benamer.py",
            "img_123456.jpg",
            "img_987654.jpg",
            "doc_peticion.doc",
            "notas.txt"
            ]
        
        self.args["lower"] = True
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_mays(self):
        file_sust_result = [
            "BENAMER.PY",
            "IMG_123456.JPG",
            "IMG_987654.JPG",
            "DOC_PETICION.DOC",
            "NOTAS.TXT"
            ]
        
        self.args["upper"] = True
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_change_ext(self):
        file_sust_result = [
            "benamer.bmp",
            "img_123456.bmp",
            "img_987654.bmp",
            "doc_peticion.bmp",
            "notas.bmp"
            ]
        
        self.args["ext"] = "bmp"
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
            
    def test_filter_by_ext(self):
        file_sust_result = [
            "benamer.py",
            "123456.jpg",
            "987654.jpg",
            "doc_peticion.doc",
            "notas.TXT"
            ]
        
        self.args["filter_by_ext"] = "jpg"
        self.args["remove_prefix"] = "img_"
        file_sust = benamer.do_subst(self.fns, self.args)
        
        for i, nf_pair in enumerate(file_sust.items()):
            self.assertEqual(self.fns[i], nf_pair[0])
            self.assertEqual(file_sust_result[i], nf_pair[1])
    
    
if __name__ == "__main__":
    unittest.main()
