# Mini-transformer CPU Adafactor vs AdamW real-corpus confirmation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `mini-transformer-cpu-adafactor-vs-adamw-real-corpus-confir-c73b6b57f1`
Run ID: `mini-transformer-cpu-adafactor-vs-adamw-real-corpus-confir-c73b6b57f1-20260620T095342083718+0000`

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

- Parent run decision: Adafactor Factored Second Moments vs AdamW on CPU Pretraining: enoch://control-plane/projects/adafactor-factored-second-moments-vs-adamw-on-cpu-pretraining-aeb892926838/runs/adafactor-factored-second-moments-vs-adamw-on-cpu-pretraining-aeb892926838-20260620T092941754538+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c2a7e9f9b68f

## What looked useful

Adafactor beat AdamW mean final validation loss by 0.0845 cross-entropy points (-3.16%) and used 17,284 optimizer-state bytes versus AdamW's 900,736 bytes in this bounded direct real-corpus test.

## Boundaries and scale limits

Single small model, one public character corpus, two seeds, one learning rate per optimizer, 100 training steps, no late-stage convergence, no downstream tasks, no LR sweep, and no larger-tokenized LLM setting.

## Claim scope

In a 112,577-parameter character-level causal Transformer trained for 100 CPU steps on Tiny Shakespeare across two seeds, PyTorch Adafactor at lr 0.01 achieved lower early validation loss than AdamW at lr 0.001 while using about 1.9% as many optimizer-state bytes.

## Why it stopped

Tier 1 direct test produced a useful positive mechanism signal, but evidence is too narrow for publication-grade optimizer claims.

## Recommended next action

Run a bounded deepen follow-up with a small LR grid, at least 5 seeds, 500-1000 steps, and a second real corpus before reconsidering any paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mini-transformer Adafactor vs AdamW LR-grid robustness on two real corpora
- Success threshold: Adafactor's best mean validation loss is within 2% of AdamW's best mean validation loss on both corpora while optimizer-state bytes remain below 10% of AdamW.
- Stop condition: Stop if Adafactor is more than 2% worse than AdamW on either corpus after the LR grid, if instability occurs in at least 2 of 5 seeds, or if the CPU-only run would exceed the local 15 minute cap without a checkpointed scale-out route.

## Evidence references

- Artifact root: `<local-path>/projects/mini-transformer-cpu-adafactor-vs-adamw-real-corpus-confir-c73b6b57f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
