# 1-bit Adam Gradient Compression for Home CPU Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-adam-gradient-compression-for-home-cpu-distributed-training-f8a69c3a27fb`
Run ID: `1-bit-adam-gradient-compression-for-home-cpu-distributed-training-f8a69c3a27fb-20260604T234816523049+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/752afe044432

## What looked useful

The naive 1-bit error-feedback Adam path is an early negative signal: it lost 6.11 absolute validation accuracy points versus dense Adam, and a 50-step dense warmup lost 15.89 points. A simpler sign+scale no-residual baseline was unexpectedly close to dense while retaining the same 31.97x payload reduction and 7.87x simulated transfer-time speedup under 20 Mbps / 25 ms assumptions.

## Boundaries and scale limits

Single-process simulation, synthetic teacher-labeled classification, 3 seeds, 300 optimizer steps, simulated home-network transfer model only; no real multi-host networking, no transformer workload, no real corpus, and no full published 1-bit Adam optimizer-state protocol.

## Claim scope

On a CPU-only NumPy synthetic 4-worker data-parallel MLP proxy, sign+scale gradient compression preserved Adam validation accuracy within 0.43 absolute points of dense Adam while cutting payload 31.97x, but the tested 1-bit worker-side error-feedback Adam variants did not preserve quality.

## Why it stopped

Proxy early falsification of the tested 1-bit error-feedback Adam implementation; useful adjacent signal exists, but direct networking/model evidence is not sufficient for a paper claim.

## Recommended next action

Stop this run as a no-paper useful signal; next, test the sign+scale Adam baseline with real multiprocessing or two-host throttled TCP allreduce on a real small dataset before revisiting more complex 1-bit Adam protocols.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-network sign+scale Adam baseline for home CPU training
- Success threshold: Sign+scale final validation accuracy within 1.0 absolute percentage point of dense Adam and measured communication time at least 5x lower, without increasing total wall time by more than 10% on the throttled setup.
- Stop condition: Stop if sign+scale loses more than 2 absolute validation accuracy points in two seeds or if measured compression overhead erases at least half of the communication-time gain.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-adam-gradient-compression-for-home-cpu-distributed-training-f8a69c3a27fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
