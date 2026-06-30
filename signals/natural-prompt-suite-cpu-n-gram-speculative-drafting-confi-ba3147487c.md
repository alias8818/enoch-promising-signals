# Natural Prompt Suite CPU N-Gram Speculative Drafting Confirmation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-prompt-suite-cpu-n-gram-speculative-drafting-confi-ba3147487c`
Run ID: `natural-prompt-suite-cpu-n-gram-speculative-drafting-confi-ba3147487c-20260604T030216591861+0000`

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

- Parent run decision: CPU N-Gram Cache Speculative Drafting: enoch://control-plane/projects/cpu-n-gram-cache-speculative-drafting-1c10ec21d00c/runs/cpu-n-gram-cache-speculative-drafting-1c10ec21d00c-20260603T212913746032+0000
- Parent run decision: Real-Model CPU N-Gram Speculative Drafting Latency Probe: enoch://control-plane/projects/real-model-cpu-n-gram-speculative-drafting-latency-probe-fdbd71f9b0/runs/real-model-cpu-n-gram-speculative-drafting-latency-probe-fdbd71f9b0-20260604T011601046157+0000

## What looked useful

Dynamic context n-grams can be a strong CPU drafter when generated continuations are locally repetitive, but initial-prompt-only n-grams are too weak on this natural prompt suite. Exact-match speculative verification held for all 300 config/prompt rows.

## Boundaries and scale limits

Single GPT-2-class target model, hand-fixed prompt suite, greedy short continuations, batch size 1, Python implementation, local GB10 CUDA verification. Not validated on larger LLMs, sampling, standardized prompt suites, multi-batch serving, production kernels, or long-context workloads.

## Claim scope

In a deterministic local harness using distilgpt2 on 60 fixed natural English prompts with 64 greedy generated tokens per prompt, dynamic CPU context n-gram speculative drafting preserved exact target-model output and reduced target calls by 69.38% mean / 72.31% median in the best n=4,k=8 configuration; static prompt-only n-gram drafting did not improve target calls.

## Why it stopped

Tier 2 direct metrics support the dynamic mechanism but also show the prompt-only control is ineffective; the evidence is too narrow for publication readiness.

## Recommended next action

Stop this run as no-paper useful evidence; deepen with standardized prompt sets and at least two additional target models before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standardized Multi-Model Dynamic N-Gram Speculative Drafting Confirmation
- Success threshold: For every tested target model, dynamic n-gram drafting must maintain 100% exact greedy equivalence and achieve at least 30% median target-call reduction versus target-only baseline, while static prompt-only and shuffled controls remain materially weaker.
- Stop condition: Stop as negative if any model fails exact greedy equivalence or if median target-call reduction is below 15% on two or more models after cache/correctness bugs are ruled out.

## Evidence references

- Artifact root: `<local-path>/projects/natural-prompt-suite-cpu-n-gram-speculative-drafting-confi-ba3147487c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
