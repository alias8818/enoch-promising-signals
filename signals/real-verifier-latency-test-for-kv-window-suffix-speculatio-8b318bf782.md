# Real verifier latency test for KV-window suffix speculation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-verifier-latency-test-for-kv-window-suffix-speculatio-8b318bf782`
Run ID: `real-verifier-latency-test-for-kv-window-suffix-speculatio-8b318bf782-20260620T130804225471+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: KV-cache n-gram suffix speculation with zero extra VRAM: enoch://control-plane/projects/kv-cache-n-gram-suffix-speculation-with-zero-extra-vram-a50cc05a86ff/runs/kv-cache-n-gram-suffix-speculation-with-zero-extra-vram-a50cc05a86ff-20260620T125253569357+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/af51574fccbe

## What looked useful

Windowing the verifier KV cache produced real attention latency speedups in 24/32 nontrivial cases, with median nontrivial speedup 2.17x and max 5.90x, but failed the fidelity threshold in 0/32 nontrivial cases; best speed-passing fidelity still had relative L2 error 0.480 and probe top-1 agreement 0.898.

## Boundaries and scale limits

Not an end-to-end speculative decoding run; no trained model logits, acceptance rates, task quality, batching, production serving stack, or learned correction mechanism were tested.

## Claim scope

Controlled Tier 1 GPU attention-kernel benchmark for naive KV-window suffix verification with synthetic random and locality-biased Q/K/V tensors at prefix lengths 1024-8192, suffix lengths 16/64, and windows 128/512/1024.

## Why it stopped

Early direct falsification of the naive mechanism: the controlled verifier attention test met latency goals but missed the pre-registered fidelity threshold in every nontrivial prefix-truncating case, so it is not paper-positive and should not be escalated as-is.

## Recommended next action

Stop this naive KV-window verifier path as no-paper evidence; if continuing, run a bounded trained-model follow-up that measures real logit/acceptance drift under suffix-window KV truncation before considering any larger serving benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained-model logit drift for KV-window suffix verification
- Success threshold: At least 1.5x median verifier latency speedup with top-1 agreement >= 0.98 or accept/reject agreement >= 0.99 and no large KL outliers on a bounded prompt set.
- Stop condition: Stop if trained-model top-1 or accept/reject agreement remains below threshold for all tested windows that provide at least 1.5x speedup.

## Evidence references

- Artifact root: `<local-path>/projects/real-verifier-latency-test-for-kv-window-suffix-speculatio-8b318bf782`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
