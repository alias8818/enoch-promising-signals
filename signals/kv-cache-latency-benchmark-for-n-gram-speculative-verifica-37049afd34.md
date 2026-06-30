# KV-cache latency benchmark for n-gram speculative verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-latency-benchmark-for-n-gram-speculative-verifica-37049afd34`
Run ID: `kv-cache-latency-benchmark-for-n-gram-speculative-verifica-37049afd34-20260612T111907221263+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: N-gram Draft Verification for Speculative Decoding Without Extra VRAM: enoch://control-plane/projects/n-gram-draft-verification-for-speculative-decoding-without-extra-vram-c29da3d54d07/runs/n-gram-draft-verification-for-speculative-decoding-without-extra-vram-c29da3d54d07-20260611T133733900797+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a96dbb23f832

## What looked useful

Across two seeds and four prefix lengths, n>=4 block verification had minimum total median speedup 2.399x and median speedup 5.594x while matching sequential outputs within 0.000244 max absolute fp16 difference. n=1 was slower/parity and n=2 was mixed.

## Boundaries and scale limits

This was an attention-only controlled microbenchmark. It did not include full transformer projections, logits, draft model cost, real token acceptance distributions, paged KV-cache layouts, multi-request batching, or serving scheduler effects.

## Claim scope

On NVIDIA GB10 with PyTorch 2.12 SDPA and synthetic fp16 KV-cache tensors shaped as batch=1, heads=16, head_dim=64, one-pass causal verification of n>=4 draft tokens reduced target attention median latency versus n sequential one-token KV-cache verification steps across prefix lengths 128, 512, 2048, and 8192.

## Why it stopped

Tier 1 direct attention benchmark supports the mechanism but is not publication-grade or end-to-end evidence under the strict paper gate.

## Recommended next action

Run a bounded end-to-end small-transformer speculative decoding follow-up that includes projections, logits, draft-model runtime, measured acceptance lengths, and compares target-step latency against a non-speculative baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-transformer n-gram speculative verification latency
- Success threshold: At accepted n>=4, speculative verification must reduce median end-to-end per accepted token latency by at least 1.25x versus sequential target decoding while n=1/n=2 are reported honestly as neutral or negative if they remain so.
- Stop condition: Stop if projection/logit/draft overhead erases the attention gain so that n>=4 end-to-end speedup is below 1.10x in two independent seeds or if correctness diverges from the baseline decode path.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-latency-benchmark-for-n-gram-speculative-verifica-37049afd34`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
