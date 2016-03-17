def check_nofiles(fat, filesize):
    assert(filesize == 1474560)
    assert(fat.bytes_per_sector == 512)
    assert(fat.sectors_per_cluster == 1)
    assert(fat.reserved_sectors == 1)
    assert(fat.num_fats == 2)
    assert(fat.max_root_dir_entries == 224)
    assert(fat.sector_count == 2880)
    assert(fat.media == 0xf0)
    assert(fat.sectors_per_fat == 9)
    assert(fat.sectors_per_track == 18)
    assert(fat.num_heads == 2)
    assert(fat.hidden_sectors == 0)
    assert(fat.total_sector_count_32 == 0)
    assert(fat.drive_num == 0)
    assert(fat.boot_sig == 41)
    assert(fat.size_in_kb == 1440)
    assert(fat.root.filename == '        ')
    assert(fat.root.extension == '   ')
