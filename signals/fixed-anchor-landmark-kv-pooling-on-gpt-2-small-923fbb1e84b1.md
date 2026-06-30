# Fixed-anchor landmark KV pooling on GPT-2-small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `fixed-anchor-landmark-kv-pooling-on-gpt-2-small-923fbb1e84b1`
Run ID: `fixed-anchor-landmark-kv-pooling-on-gpt-2-small-923fbb1e84b1-20260531T234130899768+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/14e8254f30b8

## What looked useful

Landmark pooling used about 19.70 mean slots/query and had NLL 4.4535 (delta +0.2489 vs full), while a comparable recent-window control used about 18.02 mean slots/query and had NLL 8.3510 (delta +4.1464). Anchor dropping alone was weaker than landmark pooling on the medium proxy (NLL 4.6089, delta +0.4043).

## Boundaries and scale limits

CPU-only proxy; max 1152 evaluated tokens per medium condition, 96-token context, no optimized autoregressive KV cache, no serving memory/runtime benchmark, no generation-quality evaluation, no retraining or finetuning, and no long-context robustness beyond the tested window.

## Claim scope

Pretrained GPT-2-small, no-training teacher-forced WikiText-2 proxy at 12 chunks x 96 tokens: fixed-anchor landmark KV pooling with stride 16/recent 16 substantially reduced NLL penalty versus recent-window controls at comparable compressed-cache scale, but remained worse than full attention.

## Why it stopped

Stopped after a reproducible proxy useful signal because this run does not provide direct serving-cache evidence or paper-grade robustness; the result is no-paper but worth a bounded follow-up.

## Recommended next action

Run a bounded deepen follow-up implementing true autoregressive GPT-2-small KV-cache compression at 512-1024 token contexts with equal-slot recent, anchor-drop, and landmark-pool controls plus memory/runtime accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Autoregressive equal-slot GPT-2-small landmark KV-cache benchmark
- Success threshold: Landmark pooling beats all equal-slot controls by at least 0.2 NLL and stays within +0.5 NLL of full attention while showing a real KV memory reduction at 512-token or longer contexts.
- Stop condition: Stop if landmark pooling fails to beat equal-slot controls, exceeds +0.75 NLL versus full attention at 512-token context, or implementation overhead eliminates the measured KV-cache benefit.

## Evidence references

- Artifact root: `<local-path>/projects/fixed-anchor-landmark-kv-pooling-on-gpt-2-small-923fbb1e84b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
