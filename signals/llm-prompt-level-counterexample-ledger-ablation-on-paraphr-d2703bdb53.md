# LLM prompt-level counterexample ledger ablation on paraphrased universal claims

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-prompt-level-counterexample-ledger-ablation-on-paraphr-d2703bdb53`
Run ID: `llm-prompt-level-counterexample-ledger-ablation-on-paraphr-d2703bdb53-20260630T064318666489+0000`

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

- Parent run decision: Evidence-ledger tool agent with falsifiable claim counterexamples: enoch://control-plane/projects/evidence-ledger-tool-agent-with-falsifiable-claim-counterexamples-8745bdb565a7/runs/evidence-ledger-tool-agent-with-falsifiable-claim-counterexamples-8745bdb565a7-20260629T152552710860+0000
- Parent run decision: Natural-language evidence-ledger counterexample ablation: enoch://control-plane/projects/natural-language-evidence-ledger-counterexample-ablation-bb8aeb107f/runs/natural-language-evidence-ledger-counterexample-ablation-bb8aeb107f-20260630T061138105892+0000

## What looked useful

For flan-t5-base, false-claim accuracy increased from 16.7% baseline to 57.3% with relevant ledgers, versus 26.7% with distractor ledgers; invalid-margin gains were positive on 124/150 false examples. For flan-t5-small, relevant ledgers did not help.

## Boundaries and scale limits

180 examples from synthetic claim families, two small Flan-T5 seq2seq models, deterministic valid/invalid target scoring, no human-vetted benchmark, no frontier chat model, and possible lexical overlap between claims and counterexamples.

## Claim scope

On a synthetic English universal-claim paraphrase set, a relevant counterexample-ledger prompt substantially improved false-claim rejection for google/flan-t5-base but not for google/flan-t5-small.

## Why it stopped

Bounded local evidence supports a mechanism for one small instruction model but is synthetic, model-dependent, and not publication-grade direct validation.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a larger instruction model and a human-vetted paraphrased universal-claim benchmark with lexical-overlap controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Counterexample-ledger ablation on human-vetted paraphrased universal claims
- Success threshold: Relevant ledger improves false-claim accuracy by at least 15 percentage points over both baseline and distractor while increasing true-control invalid rate by no more than 5 percentage points.
- Stop condition: Stop if the relevant ledger fails to beat distractor by at least 5 percentage points or causes more than a 10 point increase in invalid predictions on valid controls.

## Evidence references

- Artifact root: `<local-path>/projects/llm-prompt-level-counterexample-ledger-ablation-on-paraphr-d2703bdb53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
