# Online generative LLM-agent validation of minimal evidence-ledger anchors on episodic QA

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `online-generative-llm-agent-validation-of-minimal-evidence-1d9bdcf210`
Run ID: `online-generative-llm-agent-validation-of-minimal-evidence-1d9bdcf210-20260526T204621382864+0000`

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

- Parent run decision: Evidence-Ledger Agent with Compressed Episodic Anchors: enoch://control-plane/projects/evidence-ledger-agent-with-compressed-episodic-anchors-8f015817ceba/runs/evidence-ledger-agent-with-compressed-episodic-anchors-8f015817ceba-20260526T063251094295+0000
- Parent run decision: LLM agent validation of minimal evidence-ledger anchors on episodic QA: enoch://control-plane/projects/llm-agent-validation-of-minimal-evidence-ledger-anchors-on-07a4808ce0/runs/llm-agent-validation-of-minimal-evidence-ledger-anchors-on-07a4808ce0-20260526T142001330647+0000

## What looked useful

Medium fixed-seed evidence supports the evidence-selection mechanism: current relation-aware anchors preserve state better than transcript retrieval, stale anchors fail, entity-only anchors lose most of the advantage, and 10% noisy anchors remain above transcript retrieval.

## Boundaries and scale limits

Synthetic templated episodes and questions; programmatic oracle anchor extraction; deterministic answer reader; no real human-authored episodic QA and no measured LLM extraction or generation reliability.

## Claim scope

In a deterministic seeded episodic QA benchmark with 48,000 generated episodes and 4,800 current-state questions, oracle minimal relation-aware evidence-ledger anchors outperformed a lexical full-transcript retrieval baseline by 36.4 exact-match points and passed stale/noisy/relation ablations.

## Why it stopped

Tier-2 mechanism threshold was met, but publication readiness is blocked by synthetic templated data and oracle ledger extraction rather than real generative LLM-agent behavior.

## Recommended next action

Stop this run as no-paper useful signal; next run should replace oracle extraction with a local LLM anchor extractor/answer generator on the same fixed-seed benchmark plus a small human-authored paraphrase set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-extracted evidence-ledger anchors on paraphrased episodic QA
- Success threshold: LLM-extracted ledger beats transcript_top3 by >= 0.10 EM with bootstrap CI excluding zero, retains >= 0.85 anchor value F1, and reduces answer-context tokens by >= 50%.
- Stop condition: Stop as negative if LLM-extracted anchor value F1 is below 0.75 or if ledger QA does not beat transcript_top3 by at least 0.05 EM on two fixed seed sets.

## Evidence references

- Artifact root: `<local-path>/projects/online-generative-llm-agent-validation-of-minimal-evidence-1d9bdcf210`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
