# Evidence Ledger for Tiny CPU Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tiny-cpu-agent-07c941c695bb`
Run ID: `evidence-ledger-for-tiny-cpu-agent-07c941c695bb-20260528T172431118617+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8fda443b78db

## What looked useful

Across five 120-task replications, ledger exact accuracy was 1.0000 versus scratchpad 0.3367, stale-memory accuracy was 1.0000 versus 0.0050, unsupported-claim rate was 0.0000 versus 0.3767, and mean latency changed by only +0.0012 ms/task.

## Boundaries and scale limits

Five seeds of 120 synthetic tasks each; deterministic extractor agents only; no LLM behavior, real retrieval corpus, human evaluation, adversarial paraphrase, or production agent workflow was tested.

## Claim scope

In a deterministic synthetic CPU-only document QA harness, an append-only source-bound evidence ledger prevented stale inactive memory from overriding active official records and produced cited/support-hash-backed answers without measurable latency overhead.

## Why it stopped

The result is a bounded synthetic mechanism check, not direct evidence for real tiny LLM agents or real-world corpora.

## Recommended next action

Stop this run as a no-paper useful signal; deepen with a real small local LLM/tool-agent benchmark before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger around a real tiny local LLM agent
- Success threshold: Ledger variant improves unsupported-claim rate by at least 30% relative and stale-source error rate by at least 30% relative while preserving at least 95% of baseline task success and adding less than 20% median latency.
- Stop condition: Stop if the ledger mainly increases refusals, fails to improve stale-source errors by 30% relative, or requires source metadata unavailable to the agent baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tiny-cpu-agent-07c941c695bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
