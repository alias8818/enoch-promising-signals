# CPU Kernel Determinism Audit for Volunteer Training Trust

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-kernel-determinism-audit-for-volunteer-training-trust-e30e4ce7e15f`
Run ID: `cpu-kernel-determinism-audit-for-volunteer-training-trust-e30e4ce7e15f-20260620T013245838087+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f35330e45f6f

## What looked useful

CPU-only execution should not be treated as determinism by default. Reduction order and runtime scheduling policy can change or destabilize floating-point results even on one host.

## Boundaries and scale limits

No PyTorch/JAX/TensorFlow training stack was installed or tested; no end-to-end model training, dataloader concurrency, cross-machine volunteer heterogeneity, or distributed checkpoint replay was validated.

## Claim scope

On this local CPU worker, NumPy 2.4.6 float32 matmul, reduction, and softmax were bitwise repeatable across bounded fresh-process repeats and 1/2/4 thread settings, while a native OpenMP float reduction showed non-repeatability under dynamic/guided multi-thread scheduling.

## Why it stopped

Bounded local audit produced useful but non-paper evidence; result is a proxy for volunteer training trust rather than full validation.

## Recommended next action

Run a direct CPU training-step replay audit in a pinned PyTorch CPU environment, including optimizer-state hashes and deterministic versus dynamic reduction controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch CPU Training-Step Determinism Replay Audit
- Success threshold: All deterministic-control training replays produce identical hashes across at least 5 fresh processes, and at least one intentionally relaxed-control condition demonstrates either drift or a clearly documented stable result.
- Stop condition: Stop if the pinned CPU training stack cannot be installed within the CPU-only time budget or if fixed deterministic controls already fail in smoke tests.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-kernel-determinism-audit-for-volunteer-training-trust-e30e4ce7e15f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
