# Adafactor vs AdamW for 124M GPT-2: Memory and Stability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adafactor-vs-adamw-for-124m-gpt-2-memory-and-stability-f16a7857c950`
Run ID: `adafactor-vs-adamw-for-124m-gpt-2-memory-and-stability-f16a7857c950-20260611T064314415241+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f3e4b47678f8

## What looked useful

Adafactor's factored state gives a direct, large optimizer-memory reduction for GPT-2-small-class training in this implementation. In bounded synthetic tests, fixed-lr Adafactor was numerically stable and trained at least as well as AdamW, while relative-step Adafactor was stable but barely improved over 80 short-run steps.

## Boundaries and scale limits

The stability evidence is short-horizon and synthetic only. It does not validate natural-language perplexity, long pretraining stability, multiple seeds, full GPT-2 training duration, distributed training, or checkpoint/resume behavior.

## Claim scope

On a local CUDA GB10 worker, Hugging Face Adafactor for a 124,439,808-parameter GPT-2-small-class model reduced optimizer state from 949.40 MiB with AdamW to 1.23 MiB and reduced peak CUDA allocation by about 1.13 GiB at batch_size=2, seq_len=128. Fixed-lr Adafactor completed short synthetic 80-step and 60-step stress runs without non-finite loss or gradients.

## Why it stopped

The run produced direct memory evidence and proxy stability evidence, but the stability/quality claim remains synthetic and short-run rather than full validation.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a bounded natural-language corpus run before making any GPT-2 stability or quality claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language 124M GPT-2 Adafactor vs AdamW bounded stability check
- Success threshold: Adafactor completes the bounded corpus run without non-finite events, keeps validation perplexity within 5% of the best AdamW run at matched sequence-item budget, and retains at least 500 MiB lower peak CUDA allocation for the 124M model.
- Stop condition: Stop if Adafactor has repeated non-finite loss/gradients, validation perplexity is more than 10% worse than AdamW after matched tuning, or the memory advantage disappears under the chosen training stack.

## Evidence references

- Artifact root: `<local-path>/projects/adafactor-vs-adamw-for-124m-gpt-2-memory-and-stability-f16a7857c950`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
