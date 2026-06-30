# LLM-agent validation of structured evidence ledger vs free notes on contradiction-heavy multi-step QA

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `llm-agent-validation-of-structured-evidence-ledger-vs-free-b06cef26b0`
Run ID: `llm-agent-validation-of-structured-evidence-ledger-vs-free-b06cef26b0-20260611T061900726736+0000`

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

- Parent run decision: Structured Evidence Ledger vs Free Notes for Multi-Step Agents: enoch://control-plane/projects/structured-evidence-ledger-vs-free-notes-for-multi-step-agents-1c8f54869568/runs/structured-evidence-ledger-vs-free-notes-for-multi-step-agents-1c8f54869568-20260611T060231832448+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/46bcacdb967d

## What looked useful

Across 160 paired final cases, free notes reached 0.64375 overall accuracy and ledger prompting reached 0.625. On contradiction cases, free notes reached 1.0 and ledger reached 0.975. The preset +10 percentage point ledger advantage threshold was not met, and pilot visible-ledger prompts caused output-format failures.

## Boundaries and scale limits

Two 80-case synthetic seeds, one small local seq2seq instruction model, answer-only hidden-reasoning prompts for the final fair comparison; no larger chat models, real QA corpora, or externally enforced ledger state were tested.

## Claim scope

In a Tier 1 controlled synthetic two-hop QA test using google/flan-t5-base with deterministic decoding, prompt-only structured ledger instructions did not improve over prompt-only free-form notes on contradiction-heavy cases.

## Why it stopped

Direct Tier 1 controlled evidence failed to support the structured-ledger advantage threshold; this is an early bounded falsification for prompt-only ledger prompting, not a full validation across models or real datasets.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing the line, run a bounded follow-up with a tool-enforced external ledger or stronger instruction model using the same paired threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tool-enforced evidence ledger vs free notes on contradiction-heavy QA
- Success threshold: Ledger condition improves over free notes by >=10 percentage points overall and >=10 percentage points on contradiction cases across at least 160 paired cases with no increase in parse failures.
- Stop condition: Stop as unsupported if the externally enforced ledger fails either +10 percentage point threshold or introduces materially higher invalid-answer/parse-failure rates.

## Evidence references

- Artifact root: `<local-path>/projects/llm-agent-validation-of-structured-evidence-ledger-vs-free-b06cef26b0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
