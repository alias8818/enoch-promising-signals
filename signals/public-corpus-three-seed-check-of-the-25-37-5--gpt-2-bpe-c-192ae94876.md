# Public-corpus three-seed check of the 25-37.5% GPT-2 BPE code/math mixture band

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `public-corpus-three-seed-check-of-the-25-37-5--gpt-2-bpe-c-192ae94876`
Run ID: `public-corpus-three-seed-check-of-the-25-37-5--gpt-2-bpe-c-192ae94876-20260522T202327724982+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Small-model confirmation of the GPT-2 BPE code/math mixture optimum: enoch://control-plane/projects/small-model-confirmation-of-the-gpt-2-bpe-code-math-mixtur-8ace2fe4b7/runs/small-model-confirmation-of-the-gpt-2-bpe-code-math-mixtur-8ace2fe4b7-20260522T122432835811+0000
- Parent run decision: Real-tokenizer bounded confirmation of code/math mixture-ratio optimum: enoch://control-plane/projects/real-tokenizer-bounded-confirmation-of-code-math-mixture-r-7ac585faae/runs/real-tokenizer-bounded-confirmation-of-code-math-mixture-r-7ac585faae-20260522T111505361609+0000

## What looked useful

The mixture band appears target-distribution dependent. It is a reproducible compromise for text-heavy and minimax objectives, while balanced code/math/text evaluation consistently favors 75% technical data.

## Boundaries and scale limits

CPU-worker run; 240k train BPE tokens per condition; three seeds; small public corpora; count LM rather than GPT-2-small transformer; fallback GPT-2 BPE encoder used OpenAI vocabulary and merges with a stdlib regex approximation because pip/tiktoken was unavailable.

## Claim scope

Bounded public-corpus GPT-2-BPE smoothed-trigram evidence: the 25-37.5% code/math band is best across three seeds for a text-heavy 70/15/15 text/code/math target and for worst-domain NLL, but not for balanced or mean-domain evaluation.

## Why it stopped

Scoped bounded evidence is mixed and not Tier-4 paper-ready; follow-up depth is already 4, so no additional follow-up is recommended from this branch.

## Recommended next action

Stop this depth-4 branch as no-paper useful signal; the only meaningful next evidence tier is a separate GPU/datacenter transformer replication with exact tiktoken GPT-2 BPE and larger public corpora.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/public-corpus-three-seed-check-of-the-25-37-5--gpt-2-bpe-c-192ae94876`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
